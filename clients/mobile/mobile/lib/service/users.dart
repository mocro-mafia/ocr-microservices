import 'package:hive/hive.dart';

part 'users.g.dart';
@HiveType(typeId: 0)
class Users {
  @HiveField(0)
  final String email;

  @HiveField(1)
  final String password;

  Users({required this.email, required this.password});

  Map<String, dynamic> toJson() => {
    'email': email,
    'password': password,
  };

  factory Users.fromJson(Map<String, dynamic> json) {
    return Users(
      email: json['email'],
      password: json['password'],
    );
  }
}