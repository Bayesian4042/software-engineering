import { Body, Controller, Get, Post } from '@nestjs/common';
import { UserService } from './user.service';

@Controller()
export class UserController {
  constructor(private readonly userService: UserService) {}

  @Post("users")
  createUser( ): any {
    return this.userService.createUser('1');
  }
}
