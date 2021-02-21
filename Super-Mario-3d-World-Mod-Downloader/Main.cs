using System;
using System.Diagnostics;
using System.IO;
using System.IO.Compression;
using System.Threading;
using SM3DW_Keys;

namespace Super_Mario_3d_World_Mod_Downloader
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("Enter the 3DW Gamebanana download link you want to install for:");
            string link = Console.ReadLine();
            Environment.CurrentDirectory = Directory.GetCurrentDirectory();
            Process.Start("CMD.exe","curl -L "+link+" -o output.zip && exit").WaitForExit();
            Directory.CreateDirectory("Copy");
            ZipFile.ExtractToDirectory("output.zip", "Copy");
            File.Delete("output.zip");
            Console.WriteLine("Enter the region you want to install for.\n[1] USA\n[2] EUR\n[3] JPN\n");
            string choice = Console.ReadLine();
            Console.WriteLine("Enter the drive letter of your SD card;");
            string cwd = Directory.GetCurrentDirectory();
            string drive = Console.ReadLine();
            Directory.SetCurrentDirectory("Copy");
            string[] dirs = Directory.GetDirectories(Directory.GetCurrentDirectory());
            foreach (string folder in dirs)
            {
                if (Directory.Exists(folder) == true)
                {
                    Directory.SetCurrentDirectory(folder);
                    if (folder.EndsWith("content") == true)
                    {
                        goto content_folder_found;
                    } else
                    {
                        //pass
                    }
                } else
                {
                    //pass
                }
            }
        content_folder_found:
            string content_folder = Directory.GetCurrentDirectory();
            if (choice == "1")
            {
                Process.Start("CMD.exe", "robocopy \"" + content_folder + "\" \"" + drive + @"\sdcafiine\" + USA.key + @"\ModPack1\" + "content\" && exit").WaitForExit();
            } else if (choice == "2")
            {
                Process.Start("CMD.exe", "robocopy \"" + content_folder + "\" \"" + drive + @"\sdcafiine\" + EUR.key + @"\ModPack1\" + "content\" && exit").WaitForExit();
            } else if (choice == "3")
            {
                Process.Start("CMD.exe", "robocopy \"" + content_folder + "\" \"" + drive + @"\sdcafiine\" + JPN.key + @"\ModPack1\" + "content\" && exit").WaitForExit();
            } else
            {
                Environment.Exit(1);
            }
            goto complete;
        complete:
            Console.WriteLine("Complete. Exiting.");
            Directory.SetCurrentDirectory(cwd);
            Directory.Delete("Copy");
            Thread.Sleep(3000);
            Environment.Exit(0);
        }
    }
}
