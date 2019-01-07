<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);


/**
 * Get an array that represents directory tree
 * @param string $directory     Directory path
 * @param bool $recursive         Include sub directories
 * @param bool $listDirs         Include directories on listing
 * @param bool $listFiles         Include files on listing
 * @param regex $exclude         Exclude paths that matches this regex
 */
function directoryToArray($directory, $recursive = true, $listDirs = false, $listFiles = true, $exclude = '') {
    $arrayItems = array();
    $skipByExclude = false;
    $handle = opendir($directory);
    if ($handle) {
        while (false !== ($file = readdir($handle))) {
        preg_match("/(^(([\.]){1,2})$|(\.(svn|git|md))|(Thumbs\.db|\.DS_STORE))$/iu", $file, $skip);
        if($exclude){
            preg_match($exclude, $file, $skipByExclude);
        }
        if (!$skip && !$skipByExclude) {
            if (is_dir($directory. DIRECTORY_SEPARATOR . $file)) {
                if($recursive) {
                    $arrayItems = array_merge($arrayItems, directoryToArray($directory. DIRECTORY_SEPARATOR . $file, $recursive, $listDirs, $listFiles, $exclude));
                }
                if($listDirs){
                    $file = $directory . DIRECTORY_SEPARATOR . $file;
                    $arrayItems[] = $file;
                }
            } else {
                if($listFiles){
                    $file = $directory . DIRECTORY_SEPARATOR . $file;
                    $arrayItems[] = $file;
                }
            }
        }
    }
    closedir($handle);
    }
    return $arrayItems;
}

function remove_utf8_bom($text)
{
    $bom = pack('H*','EFBBBF');
    $text = preg_replace("/^$bom/", '', $text);
    return $text;
}

function file_force_contents($dir, $contents){
        $parts = explode('/', $dir);
        $file = array_pop($parts);
        $dir = '';
        foreach($parts as $part)
            if(!is_dir($dir .= "/$part")) mkdir($dir);
        file_put_contents("$dir/$file", $contents);
    }

//calls above function
$files = directoryToArray('abstracts');

//iterating through files
foreach ($files as $key => $file) {
	//the 2017 folder contains an empty file
	if (strpos($file, '2017') === false) {

		//getting contents of file
		$fileContent = remove_utf8_bom(file_get_contents('/var/www/html/prose_hen/abstract_normalizer/'.$file));

		//separating file in lines
		$lines = explode("\n", $fileContent);

		$stringNewFile = "";
		$completeDate = "";
		$separatedDate = "";
		$fileName = str_replace("..", ".", explode("/", $file)[2]) ;

		$line1 = $line2 = $line3 = $line4 = $line5 = $line6 = $line7 = $line8 = $line9 = "";

		$completeDate = explode("-", substr($fileName, 0, 10));

		if($completeDate[2] == "00")
			$completeDate[2] = "01";


		$completeDate = implode("", $completeDate)."12.0000";

		$line1 = "TOP|".$completeDate."|".$fileName.PHP_EOL;

		$line2 = "COL|Journal Abstracts, Red Hen Lab".PHP_EOL;

		$line3 = "UID|".shell_exec("uuid -n1");

		$line5 = "CMT|".PHP_EOL;

		$line6 = "CC1|ENG".PHP_EOL;

		$line9 = "END|".$completeDate."|".$fileName.PHP_EOL;

		//iterating through lines
		foreach ($lines as $index_line => $line) {

			switch (substr($line, 0, 2)) {
				case 'FN':
					# code...
					break;
				case 'PT':
					# code...
					break;
				case 'AU':
					# code...
					break;
				case 'AF':
					# code...
					break;
				case 'TI':
					$line7 = "TTL|".trim(substr($line, 2)).PHP_EOL;
					break;
				//title of the journal Abstract
				case 'SO':
					$line4 = "SRC|".trim(substr($line, 2)).PHP_EOL;
					break;
				case 'AB':
					$line8 = "CON|".trim(substr($line, 2)).PHP_EOL;
					break;
				case 'RI':
					# code...
					break;
				case 'OI':
					# code...
					break;
				case 'SN':
					# code...
					break;
				case 'EI':
					# code...
					break;
				case 'PD':
					# code...
					break;
				case 'PY':
					# code...
					break;
				case 'VL':
					# code...
					break;
				case 'IS':
					# code...
					break;
				case 'BP':
					# code...
					break;
				case 'EP':
					# code...
					break;
				case 'DI':
					# code...
					break;
				case 'UT':
					# code...
					break;
				case 'ER':
					# code...
					break;
				case 'EF':
					# code...
					break;
			}

		}

		$stringNewFile = $line1.$line2.$line3.$line4.$line5.$line6.$line7.$line8.$line9;

		// echo $stringNewFile;

		file_force_contents('/var/www/html/prose_hen/abstract_normalizer/testes/'.$file, $stringNewFile);

		echo '/var/www/html/prose_hen/abstract_normalizer/testes/'.$file."<BR>";

	}
	
}

