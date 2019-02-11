<?php
  header('Content-Type: application/json');
  
  $random = rand(1,10);
  /* Print JSON where X is a number between 1 and 10
   * {"randomNumber": X }
   */
  echo "{\"randomNumber\": " . $random . "}";