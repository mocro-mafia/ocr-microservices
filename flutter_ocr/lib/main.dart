import 'package:flutter/material.dart';
import 'package:flutter_ocr/Pages/upload_file.dart';
import 'Pages/Auth/login_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});


  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      routes: {
        '/': (context) => const LoginScreen(),
        '/upload': (context) => const UploadFile(),
      },
    );
  }
}

