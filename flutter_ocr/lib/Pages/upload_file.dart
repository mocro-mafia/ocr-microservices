import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter_ocr/Components/custom_drawer.dart';
import 'package:flutter_ocr/Services/file_upload_service.dart';
import 'package:file_picker/file_picker.dart';
import 'package:logger/logger.dart';

class UploadFile extends StatefulWidget {
  const UploadFile({super.key});

  @override
  State<UploadFile> createState() => _UploadFileState();
}

class _UploadFileState extends State<UploadFile> {
  File? _selectedFile;
  bool _isSelected = false; // Tracks upload status
  FileUploadService fileUploadService = FileUploadService();
  Logger logger = Logger();

  void _selectFile() async {
    final result = await FilePicker.platform.pickFiles();
    if (result != null && result.files.single.path != null) {
      setState(() {
        _selectedFile = File(result.files.single.path!);
        setState(() {
          _isSelected = true;
        });// Reset the upload status
        logger.i('Selected file: ${_selectedFile!.path}');
      });
    }
  }

  void _uploadFile() async {
    logger.i('Uploading file...');
    if (_selectedFile != null) {
      final response = await fileUploadService.uploadFile(_selectedFile!);
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(
              response ? 'File uploaded successfully!' : 'File upload failed!'),
        ),
      );
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Please select a file first!'),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Upload File'),

      ),
      drawer: const Customdrawer(),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            if (_selectedFile != null)
              Image.file(
                _selectedFile!,
                height: 150,
                fit: BoxFit.cover,
              )
            else
              Container(
                height: 150,
                color: Colors.grey[200],
                child: const Center(
                  child: Icon(
                    Icons.cloud_upload_outlined,
                    size: 50,
                  ),
                ),
              ),
            const SizedBox(height: 16),
            ElevatedButton.icon(
              icon: const Icon(Icons.file_upload),
              label: const Text('Select File'),
              onPressed: _selectFile,
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.black,
                foregroundColor: Colors.white,
              ),
            ),
            const SizedBox(height: 16),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                OutlinedButton(
                  onPressed: () => Navigator.pop(context),
                  child: const Text('Cancel'),
                ),
                ElevatedButton(
                  onPressed: _uploadFile,
                  style: ElevatedButton.styleFrom(
                    backgroundColor: _isSelected
                        ? Colors.white
                        : Colors.grey, // Change color based on upload status
                    foregroundColor: Colors.black,
                  ),
                  child: const Text('Submit'),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
