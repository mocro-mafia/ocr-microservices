import 'package:hive/hive.dart';

part 'user.g.dart';
@HiveType(typeId: 0)
class User {
  @HiveField(0)
  final String email;

  @HiveField(1)
  final String password;

  User({required this.email, required this.password});

  Map<String, dynamic> toJson() => {
    'email': email,
    'password': password,
  };

  factory User.fromJson(Map<String, dynamic> json) {
    return User(
      email: json['email'],
      password: json['password'],
    );
  }
}