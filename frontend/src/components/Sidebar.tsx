"use client";

import { useState } from "react";
import Link from "next/link";
import { MenuIcon, XIcon } from "lucide-react"; // XIcon for closing the sidebar
import Image from "next/image";
import MaxWidthWrapper from "./MaxWidthWrapper";
import LogoOlla from "../../public/olla-caliente.png";
import { Button } from "./ui/button";
import { cn } from "@/lib/utils";
import {
  GitHubLogoIcon,
  InstagramLogoIcon,
  TwitterLogoIcon,
} from "@radix-ui/react-icons";

const Sidebar = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="relative flex h-[6.5vh] w-full rounded-lg bg-yellow-400 shadow-xl justify-between">
      <MaxWidthWrapper className="flex items-center justify-between w-full px-4">
        <Link href="/" className="flex items-center space-x-2">
          <Image src={LogoOlla} alt="Logo" width={40} height={40} />
          <p className="font-bold text-2xl">FastFood</p>
        </Link>
        <nav className="hidden md:flex space-x-8 items-center">
          <Link href="/menu" className="text-base font-semibold">
            MENU
          </Link>
          <Link href="/signin" className="text-base font-semibold">
            UNETE
          </Link>
        </nav>
        <Button onClick={() => setIsOpen(!isOpen)} className="md:hidden">
          <MenuIcon className="w-6 h-6 text-black" />
        </Button>
      </MaxWidthWrapper>

      <div
        className={cn(
          "fixed inset-0 z-50 bg-black bg-opacity-50 transition-opacity",
          isOpen ? "opacity-100" : "opacity-0 pointer-events-none"
        )}
        onClick={() => setIsOpen(false)}
      ></div>

      <div
        className={cn(
          "fixed top-0 right-0 z-50 h-full w-64 bg-white shadow-lg transform transition-transform",
          isOpen ? "translate-x-0" : "translate-x-full"
        )}
      >
        <div className="flex items-center justify-between p-4 border-b">
          <h2 className="text-xl font-bold">FastFood</h2>
          <Button onClick={() => setIsOpen(false)}>
            <XIcon className="w-6 h-6 text-black" />
          </Button>
        </div>
        <div className="flex flex-col justify-between">
          <nav className="flex flex-col p-4 space-y-4">
            <Link href="/menu" className="text-lg font-semibold">
              MENU
            </Link>
            <Link href="/signin" className="text-lg font-semibold">
              UNETE
            </Link>
          </nav>
          <div className="p-4 mt-auto">
            <p>fastfood@email.com</p>
            <p>01 800 - 500 - 723</p>
            <div className="flex space-x-2 mt-4">
              <Link href="#">
                <InstagramLogoIcon className="w-6 h-6 text-black" />
              </Link>
              <Link href="#">
                <TwitterLogoIcon className="w-6 h-6 text-black" />
              </Link>
              <Link href="#">
                <GitHubLogoIcon className="w-6 h-6 text-black" />
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
