from utils import database
from utils import setup

#Get Startup Arguments
args = setup.startup_arguments.get();

#Setup Input Database
pathof_input_db = setup.input_db.initialize();

#Generate CSPRNG Inputs
input_db_is_generated = database.input_db.generate(args.length,args.bulk,pathof_input_db)


#Scan for breach db