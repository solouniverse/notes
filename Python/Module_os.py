#Srimatrenamaha
'''
Help on module os:

NAME
    os - OS routines for NT or Posix depending on what system we're on.

DESCRIPTION
    This exports:
      - all functions from posix or nt, e.g. unlink, stat, etc.
      - os.path is either posixpath or ntpath
      - os.name is either 'posix' or 'nt'
      - os.curdir is a string representing the current directory (always '.')
      - os.pardir is a string representing the parent directory (always '..')
      - os.sep is the (or a most common) pathname separator ('/' or '\\')
      - os.extsep is the extension separator (always '.')
      - os.altsep is the alternate pathname separator (None or '/')
      - os.pathsep is the component separator used in $PATH etc
      - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
      - os.defpath is the default search path for executables
      - os.devnull is the file path of the null device ('/dev/null', etc.)

    Programs that import and use 'os' stand a better chance of being
    portable between different platforms.  Of course, they must then
    only use functions that are defined by all platforms (e.g., unlink
    and opendir), and leave all pathname manipulation to os.path
    (e.g., split and join).
...
FUNCTIONS
    _exit(status)
        Exit to the system with specified status, without normal exit processing.

    abort()
        Abort the interpreter immediately.

        This function 'dumps core' or otherwise fails in the hardest way possible
        on the hosting operating system.  This function never returns.

    access(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True)
        Use the real uid/gid to test for access to a path.

          path
            Path to be tested; can be string or bytes
          mode
            Operating-system mode bitfield.  Can be F_OK to test existence,
            or the inclusive-OR of R_OK, W_OK, and X_OK.
          dir_fd
            If not None, it should be a file descriptor open to a directory,
            and path should be relative; path will then be relative to that
            directory.
          effective_ids
            If True, access will use the effective uid/gid instead of
            the real uid/gid.
          follow_symlinks
            If False, and the last element of the path is a symbolic link,
            access will examine the symbolic link itself instead of the file
            the link points to.

        dir_fd, effective_ids, and follow_symlinks may not be implemented
          on your platform.  If they are unavailable, using them will raise a
          NotImplementedError.

        Note that most operations will use the effective uid/gid, therefore this
          routine can be used in a suid/sgid environment to test if the invoking user
          has the specified access to the path.

    chdir(path)
        Change the current working directory to the specified path.

        path may always be specified as a string.
        On some platforms, path may also be specified as an open file descriptor.
          If this functionality is unavailable, using it raises an exception.

    chmod(path, mode, *, dir_fd=None, follow_symlinks=True)
        Change the access permissions of a file.

          path
            Path to be modified.  May always be specified as a str or bytes.
            On some platforms, path may also be specified as an open file descriptor.
            If this functionality is unavailable, using it raises an exception.
          mode
            Operating-system mode bitfield.
          dir_fd
            If not None, it should be a file descriptor open to a directory,
            and path should be relative; path will then be relative to that
            directory.
          follow_symlinks
            If False, and the last element of the path is a symbolic link,
            chmod will modify the symbolic link itself instead of the file
            the link points to.

        It is an error to use dir_fd or follow_symlinks when specifying path as
          an open file descriptor.
        dir_fd and follow_symlinks may not be implemented on your platform.
          If they are unavailable, using them will raise a NotImplementedError.

    close(fd)
        Close a file descriptor.

    cpu_count()
        Return the number of CPUs in the system; return None if indeterminable.

        This number is not equivalent to the number of CPUs the current process can
        use.  The number of usable CPUs can be obtained with
        ``len(os.sched_getaffinity(0))``

    getcwd()
        Return a unicode string representing the current working directory.

    getcwdb()
        Return a bytes string representing the current working directory.

    getenv(key, default=None)
        Get an environment variable, return None if it doesn't exist.
        The optional second argument can specify an alternate default.
        key, default and the result are str.


    getlogin()
        Return the actual login name.

    getpid()
        Return the current process id.

    getppid()
        Return the parent's process id.

        If the parent process has already exited, Windows machines will still
        return its id; others systems will return the id of the 'init' process (1).

    kill(pid, signal, /)
        Kill a process with a signal.

    link(src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True)
        Create a hard link to a file.    
        
    listdir(path=None)
        Return a list containing the names of the files in the directory.

        path can be specified as either str or bytes.  If path is bytes,
          the filenames returned will also be bytes; in all other circumstances
          the filenames returned will be str.
        If path is None, uses the path='.'.
        On some platforms, path may also be specified as an open file descriptor;\
          the file descriptor must refer to a directory.
          If this functionality is unavailable, using it raises NotImplementedError.

        The list is in arbitrary order.  It does not include the special
        entries '.' and '..' even if they are present in the directory.

    makedirs(name, mode=511, exist_ok=False)
        makedirs(name [, mode=0o777][, exist_ok=False])

        Super-mkdir; create a leaf directory and all intermediate ones.  Works like
        mkdir, except that any intermediate path segment (not just the rightmost)
        will be created if it does not exist. If the target directory already
        exists, raise an OSError if exist_ok is False. Otherwise no exception is
        raised.  This is recursive.

    mkdir(path, mode=511, *, dir_fd=None)
        Create a directory.

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.

        The mode argument is ignored on Windows.


'''
