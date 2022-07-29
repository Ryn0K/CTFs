<?php
class TimeModel
{
    public function __construct($format)
    {
        $this->format = addslashes($format);
        print_r($this->format.PHP_EOL);

        [ $d, $h, $m, $s ] = [ rand(1, 6), rand(1, 23), rand(1, 59), rand(1, 69) ];
        $this->prediction = "+${d} day +${h} hour +${m} minute +${s} second";
    }

    public function getTime()
    {
        $payload='$time = date("' . $this->format . '", strtotime("' . $this->prediction . '"));';
        print_r($payload);
        eval($payload);
        return isset($time) ? $time : 'Something went terribly wrong';
    }
}