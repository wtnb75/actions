import 'package:flutter_test/flutter_test.dart';
import 'package:dummy/main.dart';

void main() {
  testWidgets('renders dummy text', (WidgetTester tester) async {
    await tester.pumpWidget(const DummyApp());
    expect(find.text('dummy'), findsOneWidget);
  });
}
