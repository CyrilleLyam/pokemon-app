'use client';
import { Pokemon } from '@/constants/data';
import { ColumnDef } from '@tanstack/react-table';

export const columns: ColumnDef<Pokemon>[] = [
  {
    accessorKey: 'name',
    header: 'NAME'
  },
  {
    accessorKey: 'base_experience',
    header: 'BASE EXPERIENCE'
  },
  {
    accessorKey: 'height',
    header: 'HEIGHT'
  }
];
