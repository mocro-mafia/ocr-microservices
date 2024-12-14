import 'package:flutter/material.dart';
import 'package:flutter_ocr/Components/custom_drawer.dart';

class CardSummaryTest extends StatelessWidget {
  const CardSummaryTest({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Card Summary as Text'),
        actions: [
          IconButton(
            icon: const Icon(Icons.arrow_back),
            onPressed: () {
              Navigator.pop(context); // Navigate back to the previous page
            },
          ),
        ],
      ),
      drawer: const Customdrawer(),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Center(
          child: Card(
            elevation: 4,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(12),
            ),
            child: Padding(
              padding: const EdgeInsets.all(20.0),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: const [
                  Text(
                    '''
Full Name: Jonathan Mitchell
Position: Senior Product Manager
Company: logo

Contact Information:
- Email: j.mitchell@logo.com
- Phone: +1 (415) 555-0123
- Address: 123 Business Ave, San Francisco, CA 94105
- Website: www.logo.com

Additional Information:
- Department: Product Development
- Office: West Coast HQ
- Languages: English, Spanish
                    ''',
                    style: TextStyle(
                      fontSize: 16,
                      height: 1.5, // Line height for better readability
                      color: Colors.black87,
                    ),
                    textAlign: TextAlign.left, // Keep alignment consistent
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
      bottomNavigationBar: Padding(
        padding: const EdgeInsets.all(16.0),
        child: ElevatedButton.icon(
          onPressed: () {
            Navigator.pop(context); // Navigate back to the previous page
          },
          icon: const Icon(Icons.arrow_back),
          label: const Text('Go Back'),
          style: ElevatedButton.styleFrom(
            padding: const EdgeInsets.symmetric(vertical: 14),
            backgroundColor: Colors.blue,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(8),
            ),
          ),
        ),
      ),
    );
  }
}
