def update_curr(n):
    if n==0:
        return 11
    else:
        return n
def solution(numbers, hand):
    answer = ''
    curr_l = 10
    curr_r = 12
    
    for n in numbers:
        if n==0:
            n=11
        if n%3==1:
            answer=answer+'L'
            curr_l = update_curr(n)
            
        elif n%3==0:
            answer=answer+'R'
            curr_r = update_curr(n)
            
        else:
            tmp = abs(n-curr_l)
            d_l = int(tmp/3)+tmp%3
            tmp = abs(n-curr_r)
            d_r = int(tmp/3)+tmp%3
            
            if d_l<d_r:
                answer=answer+'L'
                curr_l = update_curr(n)
            elif d_r<d_l:
                answer=answer+'R'
                curr_r = update_curr(n)
            else:
                tmp_h = hand[0].upper()
                answer=answer+tmp_h
                if tmp_h == 'L':
                    curr_l = update_curr(n)
                else:
                    curr_r = update_curr(n)
    return answer