<?php

/**
 * 必要なクラスを必要な時に自動でローディングする。
 * pdb_client/libをルートディレクトリ(名前空間：pdb_client)として、ディレクトリ構造に対応した名前空間をつけること。
 *
 * ex.) pdb_client/lib/core ディレクトリ配下のクラスは下記の名前空間とする
 *        namespace pokemon_api_client\core;
 */
spl_autoload_register(function ($class) {
    $prefix = 'pokemon_api_client\\';

    if (strpos($class, $prefix) === 0) {
        $className = substr($class, strlen($prefix));
        $classFilePath = __DIR__ . '/../lib/' . str_replace('\\', '/', $className) . '.php';

        if (file_exists($classFilePath)) {
            require $classFilePath;
        }
    }
});
