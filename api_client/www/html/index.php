<?php

require_once './pokemon_api_client/config/ini.php';
//=================================================
// 詳細を取得
//=================================================
// use pokemon_api_client\pokemon\Request;
// use pokemon_api_client\pokemon\ApiClient;

// $Request = new Request(6);
// $ApiClient = new ApiClient($Request);
// $Pokemon = $ApiClient->exec();
// if (!$Pokemon->hasData()) {
//     exit();
// }
// console($Pokemon->getNumber());
// console($Pokemon->getName());
// console($Pokemon->getTypes());
// console($Pokemon->getStats());
// console($Pokemon->getTexts());
// console($Pokemon->getImages());
//=================================================
// 一覧を取得
//=================================================
// use pokemon_api_client\pokemon_list\Request;
// use pokemon_api_client\pokemon_list\ApiClient;

// $Request = new Request();
// $Request->setNumber(1);
// $Request->setNumberFrom(4);
// $Request->setNumberTo(7);
// $Request->setName('リ');
// $Request->setTypes('ひこう');
// $Request->setTypes(['くさ']);
// $Request->setHpFrom(50);
// $Request->setHpTo(100);
// $Request->setAttackFrom(50);
// $Request->setAttackTo(100);
// $Request->setDefenseFrom(50);
// $Request->setDefenseTo(100);
// $Request->setSpecialAttackFrom(50);
// $Request->setSpecialAttackTo(100);
// $Request->setSpecialDefenseFrom(50);
// $Request->setSpecialDefenseTo(100);
// $Request->setSpeedFrom(50);
// $Request->setSpeedTo(100);
// $Request->setTotalStatsFrom(300);
// $Request->setTotalStatsTo(500);
// $Request->setTexts('炎');
// $Request->setTexts(['炎', 'ツメ']);
// $Request->setTexts(['炎', '草']);
// $Request->setSort('-number');
// $Request->setOffset(10);
// $Request->setSize(10);
// $ApiClient = new ApiClient($Request);
// $PokemonList = $ApiClient->exec();
// if (!$PokemonList->hasHitData()) {
//     exit();
// }
// console($PokemonList->getTotal());
// console($PokemonList->getPage());
// console($PokemonList->getNextPageUri());
// foreach ($PokemonList->getPokemonResponses() as $Pokemon) {
//     console($Pokemon->getNumber());
//     console($Pokemon->getName());
//     console($Pokemon->getTypes());
//     console($Pokemon->getStats());
//     console($Pokemon->getTexts());
//     console($Pokemon->getImages());
//     exit();
// }
