import 'package:flutter/material.dart';
import 'ocr/upload_page.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Upload an ID',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: UploadPage(),
    );
  }
}

