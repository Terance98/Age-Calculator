##hello terance##
from datetime import datetime
now = datetime.now()
ty = now.year
tm = now.month
td = now.day
ans = "y"
while ans == 'y' or ans == 'Y':
    dob = raw_input("Enter your date of birth in dd/mm/yyyy format:")
    l = dob.split("/")
    bd = int(l[0])
    bm = int(l[1])
    by = int(l[2])
    if bm != 2 or bd != 29:
        if tm == 1 or tm == 2 or tm == 4 or tm == 6 or tm == 8 or tm == 9 or tm == 11:
            d = 31
        elif tm == 3:
            if ty % 4 == 0 and (ty % 100 != 0 and ty % 400 == 0):
                d = 29
            else:
                d = 28
        else:
            d = 30
        if by <= ty:
            def date():
                if td > bd:
                    ad = td-bd
                elif td == bd:
                    ad = 0
                else:
                    n = bd-td
                    ad = d-n
                return ad
            if tm > bm:
                if td > bd:
                    am = tm-bm
                else:
                    am = tm-bm-1
                ay = ty-by
                date()
            elif tm == bm:
                date()
                if date() == 0:
                    print "Happy Birthday"
                    am = 0
                    ay = ty-by
                else:
                    if bd < td:
                        am = 0
                        ay = ty-by
                    else:
                        am = 11
                        ay = ty-by-1
            else:
                date()
                ch = bm-tm
                if bd < td:
                    am = 12-ch
                    ay = ty-by
                else:
                    am = 11-ch
                    ay = ty-by-1
            print "\nYou are", ay, "years", am, "months and", date(), "days old."
        else:
            print "Invalid Birth year"
    else:
        print "So you are a leap year baby na,Sorry I can't calculate your age,may be 1/4th of your present age, hahahaha!"
    ans = raw_input("\nDo you wish to continue(y/n)?\n ->>")
    print "...................................................\n\n"
