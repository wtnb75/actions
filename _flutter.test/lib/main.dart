import 'package:logging/logging.dart';
import 'package:material_ui/material_ui.dart';

final log = Logger('dummy');

void main() {
  log.info('starting dummy app');
  runApp(const DummyApp());
}

class DummyApp extends StatelessWidget {
  const DummyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: Scaffold(
        body: Center(child: Text('dummy')),
      ),
    );
  }
}
