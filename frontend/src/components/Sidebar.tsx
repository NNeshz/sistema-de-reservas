"use client";

import { useState } from "react";
import Link from "next/link";
import { MenuIcon, Percent, User, Users2 } from "lucide-react";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import Image from "next/image";
import MaxWidthWrapper from "./MaxWidthWrapper";
import { buttonVariants } from "./ui/button";

const Sidebar = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="flex h-[6.5vh] w-full rounded-lg bg-yellow-500 shadow-2xl justify-between">
      <MaxWidthWrapper className="flex items-center">
        <div className="flex items-center justify-between w-full">
          <Link href={"/"} className="flex items-center gap-4">
            <Image src="/olla-caliente.png" alt="logo" width={50} height={50} />{" "}
            <p className="font-bold text-2xl">FastFood</p>
          </Link>
          <nav className="flex gap-10">
            <Link href={"/menu"} className={buttonVariants({
              variant: "ghost",
              size: "lg",
              className: "font-bold text-lg",
            })}>
              MENU
            </Link>
            <Link href={"/nosotros"} className={buttonVariants({
              variant: "ghost",
              size: "lg",
              className: "font-bold text-lg",
            })}>
              NOSOTROS
            </Link>
          </nav>
        </div>
      </MaxWidthWrapper>
    </div>
  );
};

export default Sidebar;
