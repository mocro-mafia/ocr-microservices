import 'dart:io';
import 'package:http/http.dart' as http;
import 'package:logger/logger.dart';

import '../Config/server_config.dart';

class FileUploadService {
  static final String _url = '$ipAdress/upload';
  Logger logger = Logger();

  Future<bool> uploadFile(File file) async {
    try {
      final request = http.MultipartRequest('POST', Uri.parse(_url));
      request.files.add(await http.MultipartFile.fromPath('file', file.path));

      final response = await request.send();
      return response.statusCode == 200;
    } catch (e) {
      logger.i('Error uploading file: $e');
      return false;
    }
  }
}
