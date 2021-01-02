"""Collection of useful functions"""

import functools
import hashlib
import pathlib
import pickle
import sys


class Memoizer:
    """
    Class to memoize function result on disk and, optionally, in memory.

    Check decorated function's name, arguments and keyword arguments
    to compare its results with memoized ones.

    Send message feedback to the standard error.
    """
    def __init__(self, *, cache_dir: str, in_memory: bool = True):
        """
        Initialization method.
        :param cache_dir: directory where to cache function results
            with pickle.
        :param in_memory: boolean: do you want to store results also
            in memory? Default True.
        """
        cache_dir = pathlib.Path(cache_dir)
        if not cache_dir.exists():
            print(
                f'The cache folder {cache_dir} does not exist\n'
                f"Now I'll create it at\n"
                f"{cache_dir.resolve()}\n" +
                "-" * 40,
                file=sys.stderr,
            )
            cache_dir.mkdir(parents=True)
        else:
            print(
                f"Caching at\n"
                f"{cache_dir.resolve()}\n" +
                "-" * 40
            )
        self.cache_dir = cache_dir
        self.in_memory = in_memory
        self.pickled = {}

    def memoize(self):
        """
        Use this method to make functions memoize their result
        both in memory and on disk.
        """

        def _memoize(func):
            @functools.wraps(func)
            def wrap(*args, **kwargs):
                """Actual decorator"""
                # compute the hash of the function name,
                #  arguments and keyword arguments
                str_to_digest = (
                    func.__name__ +
                    ''.join(map(str, args)) +
                    ''.join(map(str, kwargs.items()))
                ).encode('utf-8')
                hash_ = hashlib.sha256(str_to_digest).hexdigest()

                # check if the function's result has already been
                #  pickled and is in memory
                if self.in_memory:
                    if hash_ in self.pickled.keys():
                        print(
                            f'Get result of "{func.__name__}" from memory',
                            file=sys.stderr
                        )
                        return self.pickled[hash_]

                # check if the function's result has already been saved
                if (self.cache_dir / f"{hash_}.pickle").exists():
                    print(
                        f'Read result of "{func.__name__}" '
                        f'from "{hash_}.pickle"',
                        file=sys.stderr
                    )
                    with open(self.cache_dir / f"{hash_}.pickle", "rb") as f:
                        result = pickle.load(f)
                    print("Done\n" + "-" * 40, file=sys.stderr)
                    # store result into pickled files
                    self.pickled[hash_] = result
                    return result
                else:
                    result = func(*args, **kwargs)
                    print(
                        f'Save result of "{func.__name__}" '
                        f'to "{hash_}.pickle"',
                        file=sys.stderr
                    )
                    with open(self.cache_dir / f"{hash_}.pickle", "wb") as f:
                        pickle.dump(result, f)
                    print("Done\n" + "-" * 40, file=sys.stderr)
                    # store result into pickled files
                    self.pickled[hash_] = result
                    return result

            return wrap

        return _memoize
