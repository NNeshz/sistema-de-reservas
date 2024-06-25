import Link from "next/link";
import MaxWidthWrapper from "./MaxWidthWrapper";
import { Menu, ShoppingCart } from "lucide-react";
import { Sheet, SheetContent, SheetTitle, SheetTrigger } from "../ui/sheet";
import { Button, buttonVariants } from "../ui/button";

const Navbar = () => {
  return (
    <header className="md:border-b">
      {/* NAVBAR DESKTOP */}
      <MaxWidthWrapper className="hidden md:block md:py-1">
        <nav className="flex items-center justify-between">
          <div className="flex items-center gap-x-8">
            <Link href={"/"} className="text-2xl font-bold text-primary">
              FastFood
            </Link>
            <Link
              href={"/menu"}
              className="text-sm text-zinc-400 hover:text-primary"
            >
              Menu
            </Link>
            <Link
              href={"/discounts"}
              className="text-sm text-zinc-400 hover:text-primary"
            >
              Discounts
            </Link>
          </div>
          <div className="flex items-center gap-x-8">
            <Link href={"/cart"}>
              <ShoppingCart className="w-5 h-5 text-zinc-400 hover:text-primary" />
            </Link>
            <Link
              href={"/register"}
              className={buttonVariants({
                variant: "default",
                size: "sm",
              })}
            >
              Login
            </Link>
          </div>
        </nav>
      </MaxWidthWrapper>

      {/* SIDEBAR MOBILE */}
      <MaxWidthWrapper className="block py-1 md:hidden">
        <Sheet>
          <SheetTrigger asChild>
            <Button
              variant="outline"
              size="icon"
              className="shrink-0 md:hidden"
            >
              <Menu className="h-5 w-5" />
            </Button>
          </SheetTrigger>
          <SheetContent
            side="left"
            className="flex flex-col"
            aria-describedby="hola"
          >
            <SheetTitle>
              <Link href={"/"} className="text-2xl font-bold text-primary">
                FastFood
              </Link>
            </SheetTitle>
            <nav className="flex h-full flex-col justify-between">
              <div className="flex flex-col gap-y-4">
                <Link
                  href={"/menu"}
                  className="font-medium text-zinc-400 hover:text-primary"
                >
                  Menu
                </Link>
                <Link
                  href={"/discounts"}
                  className="font-medium text-zinc-400 hover:text-primary"
                >
                  Discounts
                </Link>
              </div>
              <div className="flex flex-col gap-y-4">
                <Link href={"/cart"} className="flex gap-x-3 font-semibold text-zinc-400 hover:text-primary">
                  <ShoppingCart className="w-6 h-6" /> Cart
                </Link>
                <Link
                  href={"/register"}
                  className={buttonVariants({
                    variant: "default",
                    className: "font-medium",
                  })}
                >
                  Register
                </Link>
              </div>
            </nav>
          </SheetContent>
        </Sheet>
      </MaxWidthWrapper>
    </header>
  );
};

export default Navbar;
