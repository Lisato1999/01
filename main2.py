import csv
import sys


# import numpy


def main(csvfilename, name, data, edata):
    with open(csvfilename) as fshipcsv:
        ship = csv.reader(fshipcsv)
        i = 0
        # flag = False

        for firstcolumn in ship:
            # print(firstcolumn)
            pass
            break
        lship = []
        for x in ship:
            lship.append(x)
        lfirstcolumn = []
        for x in firstcolumn:
            lfirstcolumn.append(x)
        lfirstcolumn = lfirstcolumn * len(lship)
        # array = numpy.array(lship).T
        array = lship
        # print(array)
        print(data)
        i = 0
        j = 0
        while j < len(array):
            # print(i,j)
            if i % len(firstcolumn) == 0:
                print(f"            {name}::Create([")
            for x in array[j]:
                print(f"                \"{lfirstcolumn[i]}\" => \"{x}\",")
                i += 1
            if i % len(firstcolumn) == 0:
                print("         ]);")
            # if j == len(array[j]):
            #     break
            j += 1
        print(edata)


if __name__ == '__main__':
    # ISFIRST = False
    try:
        CSVFILE = sys.argv[1]
        NAME = sys.argv[2]
        # if int(sys.argv[3]) == 1:
        #     ISFIRST = True
    except:
        print(f"{sys.argv[0]} [csv file name] [class name]")
        sys.exit(1)
    # if ISFIRST:
    DATA = """<?php

    namespace Database\Seeders;

    use Illuminate\Database\Seeder;
    class """ + NAME + """Seeder extends Seeder
    {
        /**
         * Run the database seeds.
         *
         * @return void
         */
        public function run()
        {
    """
    # else:
    #     DATA = """class """ + NAME + """Seeder extends Seeder
    # {
    #     /**
    #      * Run the database seeds.
    #      *
    #      * @return void
    #      */
    #     public function run()
    #     {
    # """
    EDATA = """
        }
    }
?>
"""

    main(CSVFILE, NAME, DATA, EDATA)
