import java.text.SimpleDateFormat;
import java.util.*;

public class FoodOrderSystem {
    private static Map<String, List<String>> ordersDatabase = new HashMap<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double totalCost = 0.0;
        List<String> orderedItems = new ArrayList<>();

        System.out.println("欢迎来到点餐系统！");
        System.out.println("菜单：");
        System.out.println("1. 汉堡包 - 10元");
        System.out.println("2. 披萨 - 20元");
        System.out.println("3. 可乐 - 5元");

        System.out.println("请选择您要点的食物（输入食物编号，输入0结束点餐）：");
        int choice = scanner.nextInt();

        while (choice != 0) {
            String item = "";
            switch (choice) {
                case 1:
                    totalCost += 10.0;
                    item = "汉堡包";
                    break;
                case 2:
                    totalCost += 20.0;
                    item = "披萨";
                    break;
                case 3:
                    totalCost += 5.0;
                    item = "可乐";
                    break;
                default:
                    System.out.println("无效的选择，请重新选择！");
            }

            orderedItems.add(item);

            System.out.println("请选择您要点的食物（输入食物编号，输入0结束点餐）：");
            choice = scanner.nextInt();
        }

        // 生成订单号
        String orderNumber = generateOrderNumber();

        // 打印客户点的食物和订单号
        System.out.println("您的订单号是：" + orderNumber);
        System.out.println("您的点单内容：");
        for (String item : orderedItems) {
            System.out.println("- " + item);
        }
        System.out.println("您的总费用为：" + totalCost + "元。谢谢光临！");

        // 存储客户点的单到数据库
        ordersDatabase.put(orderNumber, orderedItems);
        System.out.println("订单已存储在数据库中。");

        // 输出数据库中的订单信息
        System.out.println("数据库中的订单信息：");
        for (Map.Entry<String, List<String>> entry : ordersDatabase.entrySet()) {
            System.out.println("订单号：" + entry.getKey());
            System.out.println("点单内容：" + entry.getValue());
            System.out.println("----------");
        }
    }

    private static String generateOrderNumber() {
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyyMMddHHmmss");
        String date = dateFormat.format(new Date());
        return "ORDER" + date;
    }
}