#/bin/sh


if [ -z "$1" ]
  then
    INPUT_FILE="../ex02/hh_sorted.csv"  
  else
    INPUT_FILE="$1"                     
fi

OUTPUT_FILE="hh_positions.csv"



cat $INPUT_FILE \
  | head -n 1 \
  > $OUTPUT_FILE



cat $INPUT_FILE \
  | tail -n +2 \
  | awk \
    'BEGIN{
      FS=OFS="\",";

      R[0] = "[Jj]unior\\ +?/?";
      R[2] = "[Mm]iddle\\ +?/?";
      R[4] = "[Ss]enior";

    }

    {
      result = "";
      for (i = 0; i < length(R); ++i)
      {
        match($3, R[i]);
        if (RLENGTH > 0) {
          first_char = substr($3, RSTART, 1);
          result = result toupper(first_char) substr($3, RSTART + 1, RLENGTH - 1);
        }
    
      }

      if (length(result) == 0) {
        $3 = "\"-";
      }
      else {
        $3 = "\"" result;
      }
      
      print;
    }' \
  >> $OUTPUT_FILE