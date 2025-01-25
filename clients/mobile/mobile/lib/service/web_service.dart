import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;

import 'package:hive/hive.dart';

import '../model/failure.dart';
import 'users.dart';

class WebService {

  static Future<Map<String, dynamic>> login(
      String username, String password) async {
    Map<String, dynamic> result;
    Uri url = Uri.parse('http://localhost:8000/api/v1/auth/login');
    Map<String, String> data = {'username': username, 'password': password};
    try {
      var response = await http.post(url,
          body: json.encode(data),
          headers: <String, String>{'Content-Type': 'application/json'});
      if (response.statusCode == 200) {
        Users user = Users.fromJson(json.decode(response.body));
        
        // Store user data in Hive
        var box = Hive.box('userBox');
        box.put('user', user);

        result = {
          'status': true,
          'message': 'Successfully logged in.',
          'data': user
        };
      } else {
        String message = '${json.decode(response.body)['message']}.';
        result = {
          'status': false,
          'message': 'Logged in failed.',
          'data': Failure(message: message)
        };
      }
    } on SocketException {
      result = {
        'status': false,
        'message': 'Unsuccessful request.',
        'data': Failure(
            message:
                'There is not internet connection, please check your data roaming.')
      };
    }
    return result;
  }

  static Users? getStoredUser() {
    var box = Hive.box('userBox');
    return box.get('user');
  }
}