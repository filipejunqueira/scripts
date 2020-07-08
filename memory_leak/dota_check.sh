timestamp() {
  date +"%T"
}


outputfile='dota_crash.log'

while [ 1 ]
do

    echo $(timestamp) | tee -a $outputfile
    echo '#################### Memory Usage ####################################'| tee -a $outputfile
    sudo ./mem_test.sh | grep 'dota2\|steam\|gnome\|pop\|system76' | tee -a  $outputfile
    echo '####################CPU Temp##########################################'| tee -a $outputfile
    sensors | tee -a mem_dota.log | tee -a $outputfile
    echo '####################CPU Usage#########################################'| tee -a $outputfile
    sudo ./cpu_test.sh | tee -a $outputfile
    echo '####################GPU Temp##########################################'| tee -a $outputfile
    nvidia-smi | tee -a $outputfile
    sleep 1
done

