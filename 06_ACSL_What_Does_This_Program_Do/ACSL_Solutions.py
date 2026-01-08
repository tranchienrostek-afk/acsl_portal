# ACSL - What Does This Program Do? - Python Solutions

def cau_1(h=50, r=10):
    """
    Payroll calculation with overtime logic.
    h: hours worked, r: hourly rate
    """
    print("--- Câu 1 ---")
    b = 0
    if h > 48:
        b = b + (h - 48) * 2 * r
        h = 48
    if h > 40:
        b = b + (h - 40) * 1.5 * r
        h = 40
    b = b + h * r
    print(f"Output: {b}") # Expected 560.0
    return b

def cau_2():
    """
    String reversal and character matching.
    """
    print("\n--- Câu 2 ---")
    a = "BANANAS"
    num = 0
    t = ""
    # Reverse string a into t
    for j in range(len(a) - 1, -1, -1):
        t = t + a[j]
    
    # Count matching characters at same index
    for j in range(len(a)):
        if a[j] == t[j]:
            num = num + 1
    print(f"a: {a}, t: {t}")
    print(f"Output: {num}") # Expected 5
    return num

def cau_3():
    """
    List merging logic.
    """
    print("\n--- Câu 3 ---")
    A = [12, 41, 52, 57, 77, -100]
    B = [17, 34, 81]
    C = [0] * 10 
    j = 0; k = 0; n = 0
    
    try:
        # while A(k) > 0 - assuming k is the index used here as per pseudocode
        while k < len(A) and A[k] > 0:
            # while B(k) <= A(j)
            while k < len(B) and B[k] <= A[j]:
                C[n] = B[k]
                n += 1
                k += 1
            C[n] = A[j]
            n += 1
            j += 1
            if j >= len(A): break
            
        if k < len(B):
            C[n] = B[k]
    except Exception as e:
        print(f"Error in Câu 3: {e}")

    print(f"List C: {C[:n+1]}")
    print(f"Output C(4) (index 4): {C[4]}") # Expected value based on merge
    return C[4]

def cau_4():
    """
    Counting even and odd numbers from 1 to 50.
    """
    print("\n--- Câu 4 ---")
    C = 0; S = 0
    for i in range(1, 51):
        if i % 2 == 0: # i / 2 = int(i/2)
            C = C + 1
        else:
            S = S + 1
    print(f"Output C (even): {C}, S (odd): {S}") # Expected C: 25, S: 25
    return C, S

def cau_5():
    """
    Complex variable manipulation.
    """
    print("\n--- Câu 5 ---")
    a = 12; b = 1; c = 0; d = 4; e = 2
    if a > d: a = a - d                       # a = 8
    if (d - b) < (e - a): d = d + e           # 3 < -6 (False)
    
    if a * b == d * e:                        # 8 == 8 (True)
        e = (a * b) // e                       # e = 4
    else:
        d = (d * e) // a
        
    if d**2 <= (b + 1)**2:                    # 16 <= 4 (False)
        d = b + 1
    else:
        b = b + 1                              # b = 2
        
    if a + b * c == d + e * c:                # 8 + 0 == 4 + 0 (False)
        a = b * c
    else:
        d = e * c                              # d = 0
        
    res = (a + e) / b + (d + c) ** b * c 
    print(f"Output: {res}") # (8+4)/2 + (0+0)^2*0 = 6
    return res

if __name__ == "__main__":
    cau_1()
    cau_2()
    cau_3()
    cau_4()
    cau_5()
