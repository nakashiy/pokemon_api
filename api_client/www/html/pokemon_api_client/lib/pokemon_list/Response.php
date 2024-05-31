<?php

namespace pokemon_api_client\pokemon_list;

use pokemon_api_client\core\PokemonResponseBase;

class Response {
    private $total;
    private $page;
    private $next_page_uri;
    private $data;

    public function __construct($response) {
        $this->total = $response["total"];
        $this->page = $response["page"];
        $this->next_page_uri = $response["next_page_uri"];
        $pokemons = [];
        foreach ($response["data"] as $pokemon) {
            $pokemons[] = new PokemonResponseBase($pokemon);
        }
        $this->data = $pokemons;
    }

    public function hasHitData() {
        if ($this->total > 0) {
            return true;
        }
        return false;
    }
    public function getTotal() {
        return $this->total;
    }
    public function getPage() {
        return $this->page;
    }
    public function getNextPageUri() {
        return $this->next_page_uri;
    }
    public function getPokemonResponses() {
        return $this->data;
    }
}
