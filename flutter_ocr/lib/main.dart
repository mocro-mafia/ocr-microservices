import 'package:flutter/material.dart';
import 'package:flutter_ocr/Model/token_auth.dart';
import 'package:flutter_ocr/Pages/upload_file.dart';
import 'package:hive_flutter/hive_flutter.dart';
import 'Pages/Auth/login_screen.dart';


void main() async {
  await Hive.initFlutter();
  Hive.registerAdapter(AuthTokenAdapter());
  await Hive.openBox<AuthToken>('authTokenBox');
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

