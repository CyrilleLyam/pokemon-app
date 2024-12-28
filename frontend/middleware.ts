import { NextRequest, NextResponse } from 'next/server';

export function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;
  const accessToken = request.cookies.get('access_token');
  if (!accessToken && pathname !== '/login') {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  if (pathname === '/' && accessToken) {
    return NextResponse.redirect(new URL('/dashboard/overview', request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/', '/dashboard/:path*'],
};
