<?php

namespace pokemon_api_client\pokemon_list;

use pokemon_api_client\core\Constant;

class Request {
    private $number;
    private $number_from;
    private $number_to;
    private $name;
    private $types;
    private $hp_from;
    private $hp_to;
    private $attack_from;
    private $attack_to;
    private $defense_from;
    private $defense_to;
    private $special_attack_from;
    private $special_attack_to;
    private $special_defense_from;
    private $special_defense_to;
    private $speed_from;
    private $speed_to;
    private $total_stats_from;
    private $total_stats_to;
    private $texts;
    private $sort;
    private $offset;
    private $size;

    public function __construct() {
    }

    public function getURL() {
        $params = $this->getParams();
        $query = $this->getQuery($params);
        $url = Constant::END_POINT . '/pokemons' . $query;
        return $url;
    }
    private function getParams() {
        $params = [
            'number' => $this->number,
            'number_from' => $this->number_from,
            'number_to' => $this->number_to,
            'name' => $this->name,
            'types' => $this->types,
            'hp_from' => $this->hp_from,
            'hp_to' => $this->hp_to,
            'attack_from' => $this->attack_from,
            'attack_to' => $this->attack_to,
            'defense_from' => $this->defense_from,
            'defense_to' => $this->defense_to,
            'special_attack_from' => $this->special_attack_from,
            'special_attack_to' => $this->special_attack_to,
            'special_defense_from' => $this->special_defense_from,
            'special_defense_to' => $this->special_defense_to,
            'speed_from' => $this->speed_from,
            'speed_to' => $this->speed_to,
            'total_stats_from' => $this->total_stats_from,
            'total_stats_to' => $this->total_stats_to,
            'texts' => $this->texts,
            'sort' => $this->sort,
            'offset' => $this->offset,
            'size' => $this->size,
        ];
        return $params;
    }
    private function getQuery($params) {
        $query = null;
        foreach ($params as $key => $values) {
            if (is_null($values)) continue;
            if (is_array($values)) {
                foreach ($values as $value) {
                    $query .= "&{$key}=" . urlencode($value);
                }
            } else {
                $query .= "&{$key}=" . urlencode($values);
            }
        }
        return $query ? '?' . $query : '';
    }

    public function setNumber($number) {
        $this->number = $number;
    }
    public function setNumberFrom($number_from) {
        $this->number_from = $number_from;
    }
    public function setNumberTo($number_to) {
        $this->number_to = $number_to;
    }
    public function setName($name) {
        $this->name = $name;
    }
    public function setTypes($types) {
        $this->types = $types;
    }
    public function setHpFrom($hp_from) {
        $this->hp_from = $hp_from;
    }
    public function setHpTo($hp_to) {
        $this->hp_to = $hp_to;
    }
    public function setAttackFrom($attack_from) {
        $this->attack_from = $attack_from;
    }
    public function setAttackTo($attack_to) {
        $this->attack_to = $attack_to;
    }
    public function setDefenseFrom($defense_from) {
        $this->defense_from = $defense_from;
    }
    public function setDefenseTo($defense_to) {
        $this->defense_to = $defense_to;
    }
    public function setSpecialAttackFrom($special_attack_from) {
        $this->special_attack_from = $special_attack_from;
    }
    public function setSpecialAttackTo($special_attack_to) {
        $this->special_attack_to = $special_attack_to;
    }
    public function setSpecialDefenseFrom($special_defense_from) {
        $this->special_defense_from = $special_defense_from;
    }
    public function setSpecialDefenseTo($special_defense_to) {
        $this->special_defense_to = $special_defense_to;
    }
    public function setSpeedFrom($speed_from) {
        $this->speed_from = $speed_from;
    }
    public function setSpeedTo($speed_to) {
        $this->speed_to = $speed_to;
    }
    public function setTotalStatsFrom($total_stats_from) {
        $this->total_stats_from = $total_stats_from;
    }
    public function setTotalStatsTo($total_stats_to) {
        $this->total_stats_to = $total_stats_to;
    }
    public function setTexts($texts) {
        $this->texts = $texts;
    }
    public function setSort($sort) {
        $this->sort = $sort;
    }
    public function setOffset($offset) {
        $this->offset = $offset;
    }
    public function setSize($size) {
        $this->size = $size;
    }
}
