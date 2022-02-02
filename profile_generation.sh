for i in *.pssm
do
cat $i| tail -n +3|head -n -6 |tr -s " "|sed "s/\s/\t/g"> ../slides04/${i%..}.pssm
python3 pssm_parsing.py ../slides04/${i%..}.pssm  ../slides04/${i%..}.profile
done
