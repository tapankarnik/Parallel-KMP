import time
import multiprocessing
import textwrap
import math
# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
 
    # create lps[] that will hold the longest prefix suffix 
    # values for pattern
    # lps = [0]*M
    j = 0 # index for pat[]
 
    # Preprocess the pattern (calculate lps[] array)
    # computeLPSArray(pat, M, lps)
 
    i = 0 # index for txt[]
    while i < N:
        global lps
        if pat[j] == txt[i]:
            i += 1
            j += 1
 
        if j == M:
            print("Found pattern at index " + str(i-j))
            j = lps[j-1]
 
        # mismatch after j matches
        elif(i < N and pat[j] != txt[i]):
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
 
def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix
 
    # lps[0] # lps[0] is always 0
    i = 1
 
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar 
            # to search step.
            if len != 0:
                len = lps[len-1]
 
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
 
if __name__ == '__main__':
    with open('book.txt', 'r') as myfile:
        txt = myfile.read().replace('\n', '')
    pat = input('Enter the pattern: ')
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    numprocs = multiprocessing.cpu_count()
    lengthtxt = len(txt)
    M = len(pat) 
    # create lps[] that will hold the longest prefix suffix 
    # values for pattern
    lps = [0] * M
    computeLPSArray(pat, M, lps)
    print("Let us search for the pattern '"+pat+"' now")
    percorenum = math.ceil(lengthtxt / numprocs)
    txt = textwrap.wrap(txt,percorenum)

    tasks = []
    tasknum = 0
    while tasknum < numprocs:
        tasks.append((pat,txt[tasknum]))
        tasknum += 1

    # pool.starmap(KMPSearch,tasks)
    # pool.join()

    # print(txt)
    # p1 = multiprocessing.Process(target=KMPSearch, args=(pat, txt,))
    t = time.time()
    pool.starmap(KMPSearch,tasks)
    # p1.start()
    # time.sleep(20)
    # p1.join()
    # KMPSearch(pat, txt)
    print("Time taken is ",time.time()-t)
     