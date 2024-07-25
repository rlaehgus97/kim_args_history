import argparse
from kim_args_history.db.utils import count, top

def hello_msg():
    return "hello"

def cmd():
    msg = hello_msg()
    #print(msg)
    
    #argparse core functionality
    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

    parser.add_argument('-s', '--scount', type=str)           
    parser.add_argument('-t', '--top', type=int)    
    parser.add_argument('-d', '--dt', type=str)  

    args = parser.parse_args()

    if args.scount:   #args.scount == True
        # print command count
        cnt = count(args.scount)
        print(f"The command {args.scount} was used {cnt} times.")

    elif args.top:
        if args.dt:
            # print command of specific date
            print(top(args.top, args.dt))
        else:
            parser.error("error: you must use top arg with date argument")

    else:
        # print instruction
        parser.print_help()
