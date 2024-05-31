<?php

namespace pokemon_api_client\core;

use Exception;

class Curl {

    private $curl;

    public function __construct() {
        $this->curl = curl_init();
        curl_setopt($this->curl, CURLOPT_RETURNTRANSFER, true); //文字列で返す
        curl_setopt($this->curl, CURLOPT_SSL_VERIFYPEER, false); //SSL証明書の検証
        curl_setopt($this->curl, CURLOPT_SSL_VERIFYHOST, false); //SSL証明書のホストを検証
        curl_setopt($this->curl, CURLOPT_TIMEOUT, 10); //タイムアウト時間(秒)
    }

    /**
     * cURL実行
     */
    public function exec($url) {
        try {
            curl_setopt($this->curl, CURLOPT_URL, $url);
            $response = curl_exec($this->curl);
            $error_no = curl_errno($this->curl);
            $error_msg = curl_error($this->curl);
            curl_close($this->curl);
            if ($error_no !== CURLE_OK) {
                throw new Exception("エラーコード[{$error_no}]エラーメッセージ[{$error_msg}]");
            }
            return json_decode($response, true);
        } catch (Exception $e) {
            throw new Exception("cURL実行に失敗しました。:" . $e->getMessage());
        }
    }
}
