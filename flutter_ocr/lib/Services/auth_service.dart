import 'dart:convert';
import 'package:flutter_ocr/Config/server_config.dart';
import 'package:flutter_ocr/Model/token_auth.dart';
import 'package:hive/hive.dart';
import 'package:http/http.dart' as http;
import 'package:logger/logger.dart';

class AuthService {
  Logger logger = Logger();

  /// Login function to authenticate a user with their username and password.
  Future<Map<String, dynamic>> login(String username, String password) async {
    logger.i('Logging in with username: $username and password: $password');
    final url = Uri.parse(
        '$keycloakBaseUrl/realms/OCR-Realm/protocol/openid-connect/token'); 

    try {
      final response = await http.post(
        url,
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: {
          'grant_type': 'password',
          'client_id': 'Flutter-Client', 
          'username': username,
          'scope': 'email openid',
          'password': password,
        },
      );

      if (response.statusCode == 200) {
        logger.i('Login Successful: ${response.body}');
        final data = json.decode(response.body);
        final authToken = AuthToken.fromJson(data);
        logger.w('Access Token: ${authToken.accessToken}');
        
        var box = await Hive.openBox<AuthToken>('authTokenBox');
        await box.put('authToken', authToken);
        // Return the AuthToken object as a structured Map
        return {
          "result": "success",
          "authToken": authToken,
        };
      } else {
        logger.e('Login Failed: ${response.body}');
        throw Exception('Failed to login: ${response.body}');
      }
    } catch (error) {
      logger.e('An error occurred: $error');
      throw Exception('An unexpected error occurred: $error');
    }
  }

  Future<Map<String, dynamic>> signUp(String username, String email, String password) async {
    final url = Uri.parse('$keycloakBaseUrl/realms/OCR-Realm/protocol/openid-connect/register'); 

    try {
      final response = await http.post(
        url,
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: {
          'username': username,
          'email': email,
          'password': password,
        },
      ); 

      if (response.statusCode == 200) {
        logger.i('Sign Up Successful: ${response.body}'); 
        final data = json.decode(response.body);
        return data;
      } else {
        logger.e('Sign Up Failed: ${response.body}');
        throw Exception('Failed to sign up: ${response.body}');
      }
    } catch (error) {
      logger.e('An error occurred: $error');
      throw Exception('An unexpected error occurred: $error');
    }
  }
}
