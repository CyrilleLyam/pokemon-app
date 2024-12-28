import PageContainer from '@/components/layout/page-container';
import { Heading } from '@/components/ui/heading';
import { Separator } from '@/components/ui/separator';
import { ApiResponse } from '@/constants/data';
import { searchParamsCache } from '@/lib/searchparams';
import PokemonTable from './pokemon-tables';
import { API_ENDPOINTS } from '@/constants/api-endpoint';

type TPokemonListingPage = {};

export default async function PokemonListingPage({}: TPokemonListingPage) {
  const page = Number(searchParamsCache.get('page')) || 1;
  const pageSize = Number(searchParamsCache.get('limit')) || 10;
  const height = searchParamsCache.get('height');
  const baseExperience = searchParamsCache.get('base_experience');
  const order = searchParamsCache.get('sort') || 'asc';

  const queryParams = new URLSearchParams({
    page: page.toString(),
    page_size: pageSize.toString(),
    ...(height && { height: height.toString() }),
    ...(baseExperience && { base_experience: baseExperience.toString() }),
    sort_by: 'name',
    order,
  });

  const apiUrl = `${API_ENDPOINTS.BASE_URL}${API_ENDPOINTS.POKEMON.BASE}/?${queryParams.toString()}`;

  const response = await fetch(apiUrl, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
    credentials: 'include',
  });

  if (!response.ok) {
    throw new Error(`Failed to fetch data: ${response.statusText}`);
  }

  const fetchedData: ApiResponse = await response.json();

  return (
    <PageContainer scrollable>
      <div className="space-y-4">
        <div className="flex items-start justify-between">
          <Heading
            title={`Pokemon (${fetchedData.total_items})`}
            description="Manage pokemons (Server-side table functionalities.)"
          />
        </div>
        <Separator />
        <PokemonTable data={fetchedData.data} totalData={fetchedData.total_items} />
      </div>
    </PageContainer>
  );
}
