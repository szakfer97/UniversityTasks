namespace MetodaNewton
{
    class Program
    {
        static double x, xn, y, yn, epsilon;
        public static int n = 0;
        static void Main(string[] args)
        {
            xn = 2.5;
            yn = 1.5;
            epsilon = 0.00001;
            do
            {
                n++;
                x = xn; y = yn;
                double d = dfx(x, y) * dgy(x, y) - dfy(x, y) * dgx(x, y);
                double d1 = g(x, y) * dfy(x, y) - f(x, y) * dgy(x, y);
                double d2 = f(x, y) * dgx(x, y) - g(x, y) * dfx(x, y);
                xn = x + d1 / d;
                yn = y + d2 / d;
            } while (Math.Abs(xn - x) > epsilon || Math.Abs(yn - y) > epsilon);
            int res1 = Convert.ToInt32(xn);
            int res2 = Convert.ToInt32(yn);
            Console.WriteLine($"Rezultat: ({res1}, {res2}) dupa {n} iteratii.");
        }
        static double f(double x, double y)
        {
            return x * x + y * y - 10;
        }
        static double dfx(double x, double y)
        {
            return 2 * x;
        }
        static double dfy(double x, double y)
        {
            return 2 * y;
        }
        static double g(double x, double y)
        {
            return Math.Sqrt(x + y) - 2;
        }
        static double dgx(double x, double y)
        {
            return 1 / (2 * Math.Sqrt(x + y));
        }
        static double dgy(double x, double y)
        {
            return 1 / (2 * Math.Sqrt(x + y));
        }
    }
}