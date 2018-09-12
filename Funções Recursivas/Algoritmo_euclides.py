def casos(x):
    while x > 0:
        def mdc(a,d):
            r = None
            A = a
            D = d
            while r is not 0:
                r = a % d
                a = d
                d = r
            r = a
            print("MDC({},{}) = {}".format(A,D,r))
            return a
        mdc(int(input("a")),int(input("d")))
        x -= 1
casos(int(input('casos')))