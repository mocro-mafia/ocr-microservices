import 'dart:convert';
import 'package:flutter_ocr/Config/server_config.dart';
import 'package:http/http.dart' as http;
import 'package:logger/logger.dart';

class AuthService {
  Logger logger = Logger();
  Future<Map<String, dynamic>> login(String username, String password) async {
    final url = Uri.parse(
        '$keycloakBaseUrl/realms/$realm/protocol/openid-connect/token');
    final response = await http.post(
      url,
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
      body: {
        'grant_type': 'password',
        'client_id': clientId,
        'username': username,
        'password': password,
      },
    );

    if (response.statusCode == 200) {
      logger.i('Login Successful: ${response.body}');
      return json.decode(response.body);
    } else {
      logger.i('Login Failed: ${response.body}');
      throw Exception('Failed to login: ${response.body}');
    }
  }

  Future<Map<String, dynamic>> signUp(
      String username, String email, String password) async {
    final url = Uri.parse('$keycloakBaseUrl/admin/realms/$realm/users');
    final response = await http.post(
      url,
      headers: {
        'Content-Type': 'application/json',
        'Authorization':
            'Bearer <admin-access-token>' // Admin token for creating users
      },
      body: json.encode({
        'username': username,
        'email': email,
        'enabled': true,
        'credentials': [
          {'type': 'password', 'value': password, 'temporary': false}
        ]
      }),
      
    );
    logger.i("Response Body : ${response.body}");

    if (response.statusCode == 201) {
      logger.i('User created successfully');
      return {'message': 'User created successfully'};
    } else {
      logger.i('Failed to sign up: ${response.body}');
      throw Exception('Failed to sign up: ${response.body}');
    }
  }
}
