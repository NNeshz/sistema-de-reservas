import type { NextRequest } from "next/server";
import { NextResponse } from "next/server";

export function middleware(request: NextRequest) {
    const currentUser = request.cookies.get("jwt");
    const { pathname } = request.nextUrl;

    if (currentUser && (pathname.startsWith("/signin") || pathname.startsWith("/register"))) {
        return NextResponse.redirect(new URL("/", request.url));
    }

    if (!currentUser && pathname.startsWith("/profile")) {
        return NextResponse.redirect(new URL("/signin", request.url));
    }
}

export const config = {
    matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)']
};