<?php

namespace pokemon_api_client\pokemon_list;

use pokemon_api_client\core\Curl;

class ApiClient {
    private $Request;
    private $Response;

    public function __construct(Request $Request) {
        $this->Request = $Request;
    }

    public function exec() {
        $url = $this->Request->getURL();
        $Curl = new Curl();
        $response = $Curl->exec($url);
        console($url);
        console($response);
        $this->Response = new Response($response);
        return $this->Response;
    }
}
