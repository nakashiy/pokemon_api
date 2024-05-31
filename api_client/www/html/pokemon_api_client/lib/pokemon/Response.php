<?php

namespace pokemon_api_client\pokemon;

use pokemon_api_client\core\PokemonResponseBase;

/**
 * 公開DB APIのレスポンス
 */
class Response extends PokemonResponseBase {
    public function __construct($pokemon) {
        parent::__construct($pokemon);
    }
}
