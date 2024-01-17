using System;
namespace FormulaDeCuadraturaTrapez
{
    class Program
    {
        static int n;
        static double a, b, t;
        static double[]? x;
        static void Main(string[] args)
        {
            double erf25 = 0.999593047982;
            a = 0; b = (Math.PI) / 2; n = 10;
            x = new double[n + 1];
            for (int i = 0; i <= n; i++)
                x[i] = a + (i * (b - a)) / n;
            double s = 0;
            for (int i = 1; i <= n; i++)
                s += f(x[i - 1]) + f(x[i]);
            t = s * ((b - a) / (2 * n));
            Console.WriteLine("Pentru {0} subintervale, aproximarea este {1}.\n" +
                "Rezultatul corect este {2}.\n" +
                "Estimarea este {3}.", n, t, erf25, Math.Abs(erf25 - t));
            Console.WriteLine("Pamantul face {0} milioane de kilometri intr-un an", t);
            Console.ReadKey();
        }
        static double f(double x)
        {
            double c = 149.6, E = 0.016729;
            return 4 * c * Math.Sqrt(1 - Math.Pow(E, 2) * Math.Sin(x));
        }
    }
}
