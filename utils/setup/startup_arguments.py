import argparse as args

def get() -> args.ArgumentParser :
    parser = args.ArgumentParser(description="bypasswd toolchain V2 Usage")
    parser.add_argument("--length",type=int,default=10,help="Specify maximum length of generated passwords")
    parser.add_argument("--bulk",type=int,default=50,help="Specify maximum number of passwords generated in a single run")
    parser.add_argument("--update-local-db",action="store_true",help="Update the local HIBP database from before breach testing")
    parser.add_argument("--small-local-db",action="store_true",help="Use a smaller breach db , Decreases disk space but increases generation time.")
    parser.add_argument("--export-csv",action="store_true",help="Export the database as a csv")
    parser.add_argument("--export-spreadsheet",action="store_true",help="Export the database as an excel sheet")
    return parser.parse_args()


