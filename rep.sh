function replacement() {
   nln=$(nl -ba -w3 $inp | grep "${idx}" | cut -c1-3)
   oln=$((nln+lnc))
   end=$(wc -l $inp | cut -c1-3)
   #ase="s/$old/$new/$ord"
   ase="s:$old:$new:$ord"
   head -n $((oln-1))   $inp > $out
   head -n $((oln))     $inp | tail -n 1 | sed ${ase} >> $out
   tail -n $((end-oln)) $inp >> $out
#   inp=temp1
#   out=temp2
#   idx="target"
#   lnc=1           # the line you like handle relative to the line with "idx"
#   old="../old/"
#   new="../new/"
#   ord=1           # g for all, i for first, 1,2,3,4 and so on
#   replacement
} #; replacement
function addlines() {
   nln=$(nl -ba -w3 $inp | grep "${idx}" | cut -c1-3)
   oln=$((nln+lnc))
   end=$(wc -l $inp | cut -c1-3)
   head -n $((oln))   $inp > $out
   echo "line1" >> $out
   echo "line2" >> $out
   echo "line3" >> $out
   echo "line4" >> $out
   echo "line5" >> $out
   echo "line6" >> $out
   tail -n $((end-oln)) $inp >> $out
#   inp=temp1
#   out=temp2
#   idx="target"
#   lnc=2           # the line you like handle relative to the line with "idx"   
#   addlines
} #; addlines
function subtractlines() {
   nln=$(nl -ba -w3 $inp | grep "${idx}" | cut -c1-3)
   oln=$((nln+lnc))
   fln=$((oln+nls))
   end=$(wc -l $inp | cut -c1-3)
   head -n $((oln))   $inp > $out
   tail -n $((end-fln)) $inp >> $out
#   inp=temp2
#   out=temp3
#   idx="target"
#   lnc=2
#   nls=66                 #number of lines to subtract
#   subtractlines
} #; subtractlines

#   list="00"
#   list+=" 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 "
#   list+=" 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40"
#   list+=" 41 42 43 44 45 46 47 48 49 50 51 52 53 54"

   list=$(ls ./*.dat)

#   inifile=input
#   finfile=output
   for n in $list
   do 

   inp=$n
   nn=$(basename $n)

   out=temp1
   idx="target"
   lnc=0           # the line you like handle relative to the line with "idx"
   old="33"
   new="0"
   ord=1           # g for all, i for first, 1,2,3,4 and so on
   replacement

   inp=temp1
   out=temp2
   idx="targer2"
   lnc=1           # the line you like handle relative to the line with "idx"
   old="../old/"
   new="../new/"
   ord=1           # g for all, i for first, 1,2,3,4 and so on
   replacement

   inp=temp3
   out=${finfile}.$n
   idx="target3"
   lnc=0
   nls=3                 #number of lines to subtract
   subtractlines

   done
   
   rm temp*
   
