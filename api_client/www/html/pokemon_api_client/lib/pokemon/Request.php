<?php

namespace pokemon_api_client\pokemon;

use pokemon_api_client\core\Constant;

class Request {
    private $id;

    public function __construct($id) {
        $this->id = $id;
    }

    public function getURL() {
        return Constant::END_POINT . '/pokemon?id=' . $this->id;
    }
}
