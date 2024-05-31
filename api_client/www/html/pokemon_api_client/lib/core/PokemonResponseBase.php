<?php

namespace pokemon_api_client\core;

class PokemonResponseBase {
    private $number;
    private $name;
    private $types;
    private $stats;
    private $texts;
    private $images;

    public function __construct($pokemon) {
        $this->number = $pokemon["number"];
        $this->name = $pokemon["name"];
        $this->types = $pokemon["types"];
        $this->stats = $pokemon["stats"];
        $this->texts = $pokemon["texts"];
        $this->images = $pokemon["images"];
    }
    public function hasData() {
        if (is_null($this->number)) {
            return false;
        }
        return true;
    }
    public function getNumber() {
        return $this->number;
    }
    public function getName() {
        return $this->name;
    }
    public function getTypes() {
        return $this->types;
    }
    public function getStats() {
        return $this->stats;
    }
    public function getTexts() {
        return $this->texts;
    }
    public function getImages() {
        return $this->images;
    }
}
